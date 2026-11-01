/**
 * AI-Based Crop and Pest Disease Detection System - Frontend Controller
 * Manages Drag-and-Drop, WebCam Capture, Animated Scanning, and Inference API Calls.
 */

let selectedFile = null;
let cameraStream = null;
let currentFacingMode = 'environment'; // Prefer rear camera on mobile
let capturedImageData = null;

// DOM Initialization
document.addEventListener('DOMContentLoaded', () => {
    initDropzone();
});

// Switch between File Upload and Live Camera modes
function switchInputMode(mode) {
    const uploadBtn = document.getElementById('tabUploadBtn');
    const cameraBtn = document.getElementById('tabCameraBtn');
    const uploadContainer = document.getElementById('uploadModeContainer');
    const cameraContainer = document.getElementById('cameraModeContainer');

    if (mode === 'upload') {
        uploadBtn.classList.add('active');
        cameraBtn.classList.remove('active');
        uploadContainer.classList.remove('d-none');
        cameraContainer.classList.add('d-none');
        stopCamera();
    } else {
        cameraBtn.classList.add('active');
        uploadBtn.classList.remove('active');
        cameraContainer.classList.remove('d-none');
        uploadContainer.classList.add('d-none');
        startCamera();
    }
}

// Drag & Drop Configuration
function initDropzone() {
    const dropzone = document.getElementById('dropzone');
    if (!dropzone) return;

    ['dragenter', 'dragover'].forEach(eventName => {
        dropzone.addEventListener(eventName, (e) => {
            e.preventDefault();
            e.stopPropagation();
            dropzone.classList.add('dragover');
        });
    });

    ['dragleave', 'drop'].forEach(eventName => {
        dropzone.addEventListener(eventName, (e) => {
            e.preventDefault();
            e.stopPropagation();
            dropzone.classList.remove('dragover');
        });
    });

    dropzone.addEventListener('drop', (e) => {
        const dt = e.dataTransfer;
        const files = dt.files;
        if (files.length > 0) {
            handleFile(files[0]);
        }
    });
}

function handleFileSelect(event) {
    const files = event.target.files;
    if (files.length > 0) {
        handleFile(files[0]);
    }
}

function handleFile(file) {
    if (!file.type.startsWith('image/')) {
        alert('Please select a valid image file (JPG, PNG, or WEBP).');
        return;
    }
    selectedFile = file;
    capturedImageData = null;

    const reader = new FileReader();
    reader.onload = (e) => {
        showPreview(e.target.result, file.name + ' (' + (file.size / 1024).toFixed(1) + ' KB)');
    };
    reader.readAsDataURL(file);
}

// Camera Operations
async function startCamera() {
    const video = document.getElementById('webcamVideo');
    if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
        alert('Webcam streaming is not supported by your browser.');
        return;
    }

    try {
        if (cameraStream) {
            cameraStream.getTracks().forEach(t => t.stop());
        }
        cameraStream = await navigator.mediaDevices.getUserMedia({
            video: { facingMode: currentFacingMode }
        });
        video.srcObject = cameraStream;
    } catch (err) {
        console.error('Camera access error:', err);
        alert('Unable to access device camera. Please check browser permissions.');
    }
}

function switchCamera() {
    currentFacingMode = (currentFacingMode === 'user') ? 'environment' : 'user';
    startCamera();
}

function stopCamera() {
    if (cameraStream) {
        cameraStream.getTracks().forEach(t => t.stop());
        cameraStream = null;
    }
}

function takeSnapshot() {
    const video = document.getElementById('webcamVideo');
    const canvas = document.getElementById('cameraCanvas');
    if (!video || !cameraStream) return;

    canvas.width = video.videoWidth || 640;
    canvas.height = video.videoHeight || 480;
    const ctx = canvas.getContext('2d');
    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

    capturedImageData = canvas.toDataURL('image/jpeg', 0.95);
    selectedFile = null;

    stopCamera();
    document.getElementById('cameraModeContainer').classList.add('d-none');
    showPreview(capturedImageData, 'Live Camera Snapshot (' + canvas.width + 'x' + canvas.height + ')');
}

// Preview Display
function showPreview(src, metaText) {
    const previewCard = document.getElementById('previewCard');
    const imagePreview = document.getElementById('imagePreview');
    const previewMeta = document.getElementById('previewMetaText');
    const analyzeBtn = document.getElementById('analyzeBtn');

    imagePreview.src = src;
    previewMeta.innerHTML = `<i class="fa-solid fa-image me-1"></i> ${metaText}`;
    previewCard.classList.remove('d-none');
    analyzeBtn.disabled = false;

    // Scroll smoothly to preview
    previewCard.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

function resetForm() {
    selectedFile = null;
    capturedImageData = null;
    document.getElementById('fileInput').value = '';
    document.getElementById('previewCard').classList.add('d-none');
    document.getElementById('scannerOverlay').style.display = 'none';
    document.getElementById('analyzeBtn').disabled = true;
    document.getElementById('resultSummaryCol').classList.add('d-none');
    stopCamera();
    switchInputMode('upload');
}

// 1-Click Demonstration Specimen Testing
function testSample(sampleSlug) {
    resetForm();
    startScanningAnimation();

    fetch('/api/sample-detect/' + sampleSlug, { method: 'POST' })
        .then(r => r.json())
        .then(res => {
            if (!res.success) throw new Error(res.error || 'Sample diagnosis failed');
            setTimeout(() => {
                stopScanningAnimation();
                displayLiveResult(res.prediction, res.record_id);
            }, 1200);
        })
        .catch(err => {
            stopScanningAnimation();
            alert('Error running sample: ' + err.message);
        });
}

// Run AI Inference
function runDiagnosis() {
    if (!selectedFile && !capturedImageData) {
        alert('Please upload an image or take a photo first.');
        return;
    }

    startScanningAnimation();
    const formData = new FormData();

    if (selectedFile) {
        formData.append('file', selectedFile);
    } else if (capturedImageData) {
        formData.append('camera_data', capturedImageData);
    }

    fetch('/api/detect', {
        method: 'POST',
        body: formData
    })
    .then(r => r.json())
    .then(res => {
        if (!res.success) throw new Error(res.error || 'Diagnosis failed');
        setTimeout(() => {
            stopScanningAnimation();
            displayLiveResult(res.prediction, res.record_id);
        }, 1500);
    })
    .catch(err => {
        stopScanningAnimation();
        alert('Diagnosis error: ' + err.message);
    });
}

// Laser Scanning Animation Orchestration
let scanStepInterval = null;

function startScanningAnimation() {
    const overlay = document.getElementById('scannerOverlay');
    const analyzeBtn = document.getElementById('analyzeBtn');
    const statusText = document.getElementById('scanStatusText');
    const progressBar = document.getElementById('scanProgressBar');

    overlay.style.display = 'block';
    analyzeBtn.disabled = true;
    analyzeBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin me-2"></i> Analyzing Specimen...';

    const steps = [
        { text: "Converting input tensor & normalizing ImageNet distribution...", progress: "25%" },
        { text: "Extracting InvertedResidual deep spatial feature maps...", progress: "55%" },
        { text: "Evaluating calibrated temperature-scaled softmax...", progress: "80%" },
        { text: "Synthesizing agronomic dossier & pathogen epidemiology...", progress: "95%" }
    ];

    let currentStep = 0;
    progressBar.style.width = steps[0].progress;
    statusText.textContent = steps[0].text;

    scanStepInterval = setInterval(() => {
        currentStep++;
        if (currentStep < steps.length) {
            progressBar.style.width = steps[currentStep].progress;
            statusText.textContent = steps[currentStep].text;
        }
    }, 400);
}

function stopScanningAnimation() {
    if (scanStepInterval) clearInterval(scanStepInterval);
    document.getElementById('scannerOverlay').style.display = 'none';
    const analyzeBtn = document.getElementById('analyzeBtn');
    analyzeBtn.disabled = false;
    analyzeBtn.innerHTML = '<i class="fa-solid fa-wand-magic-sparkles me-2"></i> Analyze Image with AI';
}

// Display Result in Side Card
function displayLiveResult(pred, recordId) {
    const resultCol = document.getElementById('resultSummaryCol');
    const badge = document.getElementById('resCategoryBadge');

    document.getElementById('resDiagnosisName').textContent = pred.name;
    document.getElementById('resScientificName').textContent = pred.scientific_name || '';
    document.getElementById('resCropName').textContent = 'Host: ' + (pred.crop_name || 'N/A');
    document.getElementById('resConfidenceText').textContent = pred.confidence_percent + '%';
    document.getElementById('resConfidenceBar').style.width = pred.confidence_percent + '%';

    document.getElementById('resHealthStatus').textContent = pred.is_healthy ? 'Normal Vigorous Foliage' : (pred.is_unknown ? 'Unverified / OOD' : 'Pathogen / Pest Affected');
    document.getElementById('resCategoryLabel').textContent = pred.category;
    document.getElementById('resSeverityLabel').textContent = pred.severity_level || 'Moderate';

    // Style Badge
    badge.className = 'badge-category';
    if (pred.category === 'Healthy Crop') {
        badge.classList.add('badge-healthy');
    } else if (pred.category === 'Pest Infestation') {
        badge.classList.add('badge-pest');
    } else if (pred.category.includes('Fungal')) {
        badge.classList.add('badge-fungal');
    } else if (pred.category.includes('Bacterial')) {
        badge.classList.add('badge-bacterial');
    } else if (pred.category.includes('Viral')) {
        badge.classList.add('badge-viral');
    } else {
        badge.classList.add('badge-unknown');
    }
    badge.textContent = pred.category;

    // Set link to full dossier page
    const dossierBtn = document.getElementById('viewDossierBtn');
    dossierBtn.href = '/result/' + recordId;

    resultCol.classList.remove('d-none');
    resultCol.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

