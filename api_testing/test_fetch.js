const fs = require("fs");
const FormData = require("form-data");

async function sendRequest() {
    const fetch = (await import("node-fetch")).default; // Dynamic import for ES module
    const API_URL = "https://document-classifier-hpge.onrender.com/predict";
    const filePath = "test_file.pdf";
    // eg : filePath= "/home/user/desktop/filename.pdf"  
    // file location or file in present in current directory

    const form = new FormData();
    form.append("file", fs.createReadStream(filePath));

    try {
        const response = await fetch(API_URL, { method: "POST", body: form });
        const data = await response.json();
        console.log(data);
    } catch (error) {
        console.error("Error:", error);
    }
}

sendRequest();
