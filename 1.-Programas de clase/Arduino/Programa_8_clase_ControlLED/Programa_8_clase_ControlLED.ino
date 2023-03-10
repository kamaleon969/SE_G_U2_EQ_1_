int led=2;

void setup() {
  pinMode(led,OUTPUT);
  Serial.begin(9600);
  Serial.setTimeout(100);//ms por defecto son 1000
}

void loop() {
  if(Serial.available()>0){
    int v = Serial.readString().toInt();
    digitalWrite(led,v);
  }
  delay(10);
}
