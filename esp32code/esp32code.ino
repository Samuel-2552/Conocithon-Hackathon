#include <WiFi.h>
#include <WebSocketsServer.h>

WebSocketsServer webSocket = WebSocketsServer(81); // Create a WebSocket server on port 81

// Define the pin numbers for the IR sensor and LED
int irPin = 12;
int ledPin = 2;

// Replace with your network credentials
const char* ssid = "PSRAJAN@2.4G";
const char* password = "98403(&*)!";

void setup() {
   // Initialize the IR sensor and LED pins
  pinMode(irPin, INPUT);
  pinMode(ledPin, OUTPUT);
  Serial.begin(115200);
  delay(1000);

  // Connect to WiFi network
  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
  webSocket.begin(); // Start the WebSocket server  
}

void loop() {

  webSocket.loop(); // Handle incoming WebSocket connections

  int sensorData = getSensorData(); // Get sensor data (replace with your own function)
  webSocket.broadcastTXT(String(sensorData)); // Send sensor data to all connected WebSocket clients
}
  
int getSensorData()  {// Check if an object is detected by the IR sensor
  if (digitalRead(irPin) == HIGH) {
    // If an object is detected, turn on the LED
    digitalWrite(ledPin, HIGH);
  } else {
    // If no object is detected, turn off the LED
    digitalWrite(ledPin, LOW);
  }
  delay(100);
  return digitalRead(irPin)
}
