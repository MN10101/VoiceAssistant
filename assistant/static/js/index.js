// Get the circle element
const circle = document.querySelector('.circle');

// Request microphone access when the page loads
navigator.mediaDevices.getUserMedia({ audio: true })
    .then((stream) => {
        console.log("Microphone access granted.");

        // Set up the Web Audio API
        const audioContext = new (window.AudioContext || window.webkitAudioContext)();
        const analyser = audioContext.createAnalyser();
        analyser.fftSize = 256;

        // Connect the microphone input to the analyser
        const source = audioContext.createMediaStreamSource(stream);
        source.connect(analyser);

        // Analyze the audio data
        const dataArray = new Uint8Array(analyser.frequencyBinCount);

        function updateCircle() {
            analyser.getByteFrequencyData(dataArray);

            // Calculate the average volume
            const averageVolume = dataArray.reduce((sum, value) => sum + value, 0) / dataArray.length;

            // Scale the circle based on the volume
            const scale = 0.8 + (averageVolume / 128); 
            circle.style.transform = `scale(${scale})`;

            // Continuously update the circle
            requestAnimationFrame(updateCircle);
        }

        // Start the animation
        updateCircle();

        // Automatically send start message once microphone access is granted
        startAssistant();
    })
    .catch((error) => {
        console.error("Microphone access denied:", error);
        document.getElementById("output").innerText = "Microphone access denied. Please allow microphone access to use the voice assistant.";
    });

const socket = new WebSocket('ws://127.0.0.1:8000/ws/assistant/');

socket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    document.getElementById("output").innerText = data.message;
};

socket.onclose = function(e) {
    console.error('WebSocket closed unexpectedly');
    document.getElementById("output").innerText = "WebSocket connection closed.";
};

function startAssistant() {
    document.getElementById("listening-indicator").style.display = "block";
    const message = "start";
    socket.send(JSON.stringify({
        'message': message
    }));
}
