// Listener واحد فقط للـ form
document.getElementById('scanForm').addEventListener('submit', async function(e) {
    e.preventDefault();

    // جلب القيم من الحقول
    const api_url = document.getElementById('api_url').value;
    const auth_type = document.getElementById('auth_type').value;
    const auth_token = document.getElementById('auth_token').value;
    const scan_type = document.getElementById('scan_type').value;

    // تجهيز البيانات للإرسال
    const formData = new URLSearchParams();
    formData.append('api_url', api_url);
    formData.append('auth_type', auth_type);
    formData.append('auth_token', auth_token);
    formData.append('scan_type', scan_type);

    // إظهار رسالة انتظار
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = `<p>Scanning... 🔍</p>`;

    try {
        // إرسال الطلب للـ backend
        const response = await fetch('http://127.0.0.1:8000/scan', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: formData.toString()
        });

        const data = await response.json();

        // عرض النتيجة بشكل احترافي
        if(data.status === "success") {
            resultDiv.innerHTML = `
                <div style="background:#f4f4f4; padding:15px; border-radius:8px;">
                    <p><strong>API URL:</strong> ${api_url}</p>
                    <p><strong>Scan Type:</strong> ${scan_type.toUpperCase()}</p>
                    <p><strong>Result:</strong> ${data.result}</p>
                </div>
            `;
        } else {
            resultDiv.innerHTML = `<p style="color:red;">Error: ${data.message}</p>`;
        }

    } catch (err) {
        resultDiv.innerHTML = `<p style="color:red;">Error: ${err}</p>`;
    }
});
