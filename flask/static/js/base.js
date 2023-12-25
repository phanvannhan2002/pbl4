let sidebar = document.querySelector(".sidebar");
let closeBtn = document.querySelector("#btn");
let searchBtn = document.querySelector(".bx-search");

closeBtn.addEventListener("click", () => {
    sidebar.classList.toggle("open");
    menuBtnChange();//calling the function(optional)
});

searchBtn.addEventListener("click", () => { // Sidebar open when you click on the search iocn
    sidebar.classList.toggle("open");
    menuBtnChange(); //calling the function(optional)
});

// following are the code to change sidebar button(optional)
function menuBtnChange() {
    if (sidebar.classList.contains("open")) {
        closeBtn.classList.replace("bx-menu", "bx-menu-alt-right");//replacing the iocns class
    } else {
        closeBtn.classList.replace("bx-menu-alt-right", "bx-menu");//replacing the iocns class
    }
}

const camera_container = document.querySelector('.get-image')
const img_1 = document.getElementById("ESP32-1");
var imageFrame;

const WS_URL = 'ws:///172.20.10.2:8888'; // Thay đổi địa chỉ WebSocket ở đây
const ws = new WebSocket(WS_URL);
let urlObject_1;

window["cam_1_enabler"] = false;


const camera = document.querySelector('.camera');
camera.addEventListener('click', function () {
    if(camera_container.classList.contains(('camera_active'))) {
        camera_container.classList.remove('camera_active');
        window["cam_1_enabler"] = false;
    } else {
        camera_container.classList.add('camera_active');
        window["cam_1_enabler"] = true;
    }
})

function saveFunc(source) {
    var blobUrl = source === "cam_1_enabler" ? img_1.src : img_2.src;
    if (blobUrl.indexOf("blob") == -1) {
        return;
    }
    var fileName = getFomattedTime(source === "cam_1_enabler" ? "ESP32CAM1" : "ESP32CAM2") + ".jpeg";
    forceDownload(blobUrl, fileName);
}

function forceDownload(url, folderPath, fileName) {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", url, true);
    xhr.responseType = "blob";
    xhr.onload = function () {
        var blobData = xhr.response;

        // Gửi dữ liệu blob đến Flask
        fetch('/getImage', {
            method: 'POST',
            body: blobData
        })
        .then(response => response.text())
        .then(filePath => {
            console.log(filePath)
            window.location.href = ("http://127.0.0.1:5000/?flower=" + filePath);
        });
    };
    xhr.send();
}

function getFomattedTime(camInfo) {
    var today = new Date();
    var y = today.getFullYear();
    var m = today.getMonth() + 1;
    var d = today.getDate();
    var h = today.getHours();
    var mi = today.getMinutes();
    var s = today.getSeconds();
    return camInfo + "-" + y + "-" + m + "-" + d + "-" + h + "-" + mi + "-" + s;
}

function buttonFunc(source) {
    var x = document.getElementById(source);
    if (x.innerHTML === "Chụp lại") {
        x.innerHTML = "Chụp";
        window[source] = true;
    } else {
        x.innerHTML = "Chụp lại";
        window[source] = false;
    }
}

ws.onopen = () => {
    console.log(`Connected to ${WS_URL}`);
    ws.send("WEB_CLIENT");
};

ws.onmessage = async (message) => {
    const arrayBuffer = message.data;

    var blobObj = new Blob([arrayBuffer]);
    const buf = await blobObj.arrayBuffer();
    var uint8 = new Uint8Array(buf.slice(12, 13));
    var currentCam = uint8[0];
    imageFrame = img_1;
    if (!window["cam_1_enabler"]) return;
    if (urlObject_1) {
        URL.revokeObjectURL(urlObject_1);
    }
    urlObject_1 = URL.createObjectURL(blobObj);
    imageFrame.src = urlObject_1;
}
