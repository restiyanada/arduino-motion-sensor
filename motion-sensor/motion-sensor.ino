const int PIR= A5;
const int Pinled = 13;


void setup() {
  Serial.begin (9600);
  pinMode (Pinled,OUTPUT);
  pinMode (PIR,INPUT);
}

void loop() {
  int dataPIR = analogRead(PIR);
  if(dataPIR>0){
    digitalWrite(Pinled, HIGH);
    Serial.println(dataPIR);
    delay(100); 
    }
    else{
    digitalWrite(Pinled, LOW);
    Serial.println(dataPIR);
    delay(100); 
    }
}

