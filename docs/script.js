// 全局变量
let currentFiles = [];
let processedImages = [];

// 初始化
document.addEventListener('DOMContentLoaded', function () {
    initializeEventListeners();
});

function initializeEventListeners() {
    const uploadArea = document.getElementById('uploadArea');
    const fileInput = document.getElementById('fileInput');
    const processBtn = document.getElementById('processBtn');
    const downloadZipBtn = document.getElementById('downloadZipBtn');
    const downloadPdfBtn = document.getElementById('downloadPdfBtn');

    // 文件上传事件
    uploadArea.addEventListener('click', () => fileInput.click());
    uploadArea.addEventListener('dragover', handleDragOver);
    uploadArea.addEventListener('dragleave', handleDragLeave);
    uploadArea.addEventListener('drop', handleDrop);
    fileInput.addEventListener('change', handleFileSelect);

    // 处理按钮事件
    processBtn.addEventListener('click', processImages);
    downloadZipBtn.addEventListener('click', downloadZip);
    downloadPdfBtn.addEventListener('click', downloadPDF);
}

// 拖拽处理
function handleDragOver(e) {
    e.preventDefault();
    e.stopPropagation();
    e.currentTarget.classList.add('dragover');
}

function handleDragLeave(e) {
    e.preventDefault();
    e.stopPropagation();
    e.currentTarget.classList.remove('dragover');
}

function handleDrop(e) {
    e.preventDefault();
    e.stopPropagation();
    e.currentTarget.classList.remove('dragover');

    const files = Array.from(e.dataTransfer.files);
    handleFiles(files);
}

function handleFileSelect(e) {
    const files = Array.from(e.target.files);
    handleFiles(files);
}

function handleFiles(files) {
    // 过滤图片文件
    const imageFiles = files.filter(file => file.type.startsWith('image/'));

    if (imageFiles.length === 0) {
        alert('请选择图片文件！');
        return;
    }

    currentFiles = imageFiles;
    showSettings();

    // 更新上传区域显示
    const uploadArea = document.getElementById('uploadArea');
    uploadArea.innerHTML = `
        <div class="upload-content">
            <div class="upload-icon">✅</div>
            <h3>已选择 ${imageFiles.length} 个图片文件</h3>
            <p>${imageFiles.map(f => f.name).join(', ')}</p>
            <p>点击下方"开始切分"按钮处理图片</p>
        </div>
    `;
}

function showSettings() {
    document.getElementById('settingsSection').style.display = 'block';
    document.getElementById('progressSection').style.display = 'none';
    document.getElementById('resultsSection').style.display = 'none';
}

async function processImages() {
    const maxHeight = parseInt(document.getElementById('maxHeight').value);
    const processBtn = document.getElementById('processBtn');

    // 禁用按钮，显示进度
    processBtn.disabled = true;
    processBtn.innerHTML = '<span class="spinner"></span>处理中...';

    showProgress();
    processedImages = [];

    try {
        for (let i = 0; i < currentFiles.length; i++) {
            const file = currentFiles[i];
            updateProgress((i / currentFiles.length) * 100, `正在处理: ${file.name}`);

            const splitImages = await splitImage(file, maxHeight);
            processedImages.push({
                originalFile: file,
                splitImages: splitImages
            });

            // 添加小延时让用户看到进度
            await new Promise(resolve => setTimeout(resolve, 100));
        }

        updateProgress(100, '处理完成！');
        showResults();

    } catch (error) {
        console.error('处理图片时出错:', error);
        alert('处理图片时出错: ' + error.message);
    } finally {
        processBtn.disabled = false;
        processBtn.innerHTML = '🔪 开始切分';
    }
}

function showProgress() {
    document.getElementById('progressSection').style.display = 'block';
    document.getElementById('resultsSection').style.display = 'none';
}

function updateProgress(percent, text) {
    document.getElementById('progressFill').style.width = percent + '%';
    document.getElementById('progressText').textContent = text;
}

async function splitImage(file, maxHeight) {
    return new Promise((resolve, reject) => {
        const img = new Image();
        img.onload = function () {
            try {
                const canvas = document.createElement('canvas');
                const ctx = canvas.getContext('2d');

                const originalWidth = img.width;
                const originalHeight = img.height;

                // 计算需要切分的片数
                const numSlices = Math.ceil(originalHeight / maxHeight);
                const splitImages = [];

                for (let i = 0; i < numSlices; i++) {
                    // 计算当前切片的高度
                    const sliceTop = i * maxHeight;
                    const sliceHeight = Math.min(maxHeight, originalHeight - sliceTop);

                    // 设置canvas尺寸
                    canvas.width = originalWidth;
                    canvas.height = sliceHeight;

                    // 清空canvas
                    ctx.clearRect(0, 0, canvas.width, canvas.height);

                    // 绘制图片切片
                    ctx.drawImage(
                        img,
                        0, sliceTop, originalWidth, sliceHeight, // 源区域
                        0, 0, originalWidth, sliceHeight         // 目标区域
                    );

                    // 转换为blob
                    canvas.toBlob(blob => {
                        splitImages.push({
                            blob: blob,
                            filename: `${getBaseName(file.name)}_part_${(i + 1).toString().padStart(2, '0')}.png`,
                            width: originalWidth,
                            height: sliceHeight,
                            index: i + 1
                        });

                        // 当所有切片完成时resolve
                        if (splitImages.length === numSlices) {
                            resolve(splitImages);
                        }
                    }, 'image/png', 0.9);
                }
            } catch (error) {
                reject(error);
            }
        };

        img.onerror = () => reject(new Error('无法加载图片'));
        img.src = URL.createObjectURL(file);
    });
}

function getBaseName(filename) {
    return filename.substring(0, filename.lastIndexOf('.')) || filename;
}

function showResults() {
    document.getElementById('resultsSection').style.display = 'block';

    // 计算统计信息
    const totalImages = processedImages.reduce((sum, item) => sum + item.splitImages.length, 0);
    const originalCount = processedImages.length;

    // 更新结果摘要
    const summaryEl = document.getElementById('resultsSummary');
    summaryEl.innerHTML = `
        <h4>📊 处理统计</h4>
        <p>原始图片: ${originalCount} 个</p>
        <p>切分后图片: ${totalImages} 个</p>
        <p>平均每张切分为: ${Math.round(totalImages / originalCount)} 个片段</p>
    `;

    // 生成预览
    generatePreview();
}

function generatePreview() {
    const previewGrid = document.getElementById('previewGrid');
    previewGrid.innerHTML = '';

    processedImages.forEach(item => {
        item.splitImages.forEach(splitImage => {
            const previewItem = document.createElement('div');
            previewItem.className = 'preview-item';

            const img = document.createElement('img');
            img.src = URL.createObjectURL(splitImage.blob);
            img.alt = splitImage.filename;

            const info = document.createElement('div');
            info.className = 'preview-info';
            info.innerHTML = `
                <strong>${splitImage.filename}</strong><br>
                ${splitImage.width} × ${splitImage.height}px
            `;

            previewItem.appendChild(img);
            previewItem.appendChild(info);
            previewGrid.appendChild(previewItem);
        });
    });
}

async function downloadZip() {
    try {
        // 如果JSZip还没加载，动态加载
        if (typeof JSZip === 'undefined') {
            await loadJSZip();
        }

        const zip = new JSZip();

        // 添加所有切分的图片到ZIP
        processedImages.forEach(item => {
            const folderName = getBaseName(item.originalFile.name);
            const folder = zip.folder(folderName);

            item.splitImages.forEach(splitImage => {
                folder.file(splitImage.filename, splitImage.blob);
            });
        });

        // 生成ZIP文件
        const zipBlob = await zip.generateAsync({ type: 'blob' });

        // 下载
        const downloadLink = document.createElement('a');
        downloadLink.href = URL.createObjectURL(zipBlob);
        downloadLink.download = 'split_images.zip';
        downloadLink.click();

    } catch (error) {
        console.error('生成ZIP文件时出错:', error);
        alert('生成ZIP文件时出错: ' + error.message);
    }
}

function loadJSZip() {
    return new Promise((resolve, reject) => {
        const script = document.createElement('script');
        script.src = 'https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js';
        script.onload = resolve;
        script.onerror = reject;
        document.head.appendChild(script);
    });
}

async function downloadPDF() {
    try {
        const { jsPDF } = window.jspdf;

        for (let fileIndex = 0; fileIndex < processedImages.length; fileIndex++) {
            const item = processedImages[fileIndex];
            const pdf = new jsPDF();
            let isFirstPage = true;

            for (const splitImage of item.splitImages) {
                if (!isFirstPage) {
                    pdf.addPage();
                }

                // 计算PDF页面尺寸
                const pageWidth = pdf.internal.pageSize.getWidth();
                const pageHeight = pdf.internal.pageSize.getHeight();

                // 计算图片缩放比例
                const imgRatio = splitImage.width / splitImage.height;
                const pageRatio = pageWidth / pageHeight;

                let imgWidth, imgHeight;
                if (imgRatio > pageRatio) {
                    imgWidth = pageWidth - 20; // 留边距
                    imgHeight = imgWidth / imgRatio;
                } else {
                    imgHeight = pageHeight - 20; // 留边距
                    imgWidth = imgHeight * imgRatio;
                }

                // 居中位置
                const x = (pageWidth - imgWidth) / 2;
                const y = (pageHeight - imgHeight) / 2;

                // 将blob转换为base64
                const base64 = await blobToBase64(splitImage.blob);

                // 添加图片到PDF
                pdf.addImage(base64, 'PNG', x, y, imgWidth, imgHeight);
                isFirstPage = false;
            }

            // 下载PDF
            const fileName = `${getBaseName(item.originalFile.name)}_merged.pdf`;
            pdf.save(fileName);
        }

    } catch (error) {
        console.error('生成PDF时出错:', error);
        alert('生成PDF时出错: ' + error.message);
    }
}

function blobToBase64(blob) {
    return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.onload = () => resolve(reader.result);
        reader.onerror = reject;
        reader.readAsDataURL(blob);
    });
}

// 添加一些实用工具函数
function formatFileSize(bytes) {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
}

// 添加错误处理
window.addEventListener('error', function (e) {
    console.error('JavaScript错误:', e.error);
});

window.addEventListener('unhandledrejection', function (e) {
    console.error('未处理的Promise拒绝:', e.reason);
}); 