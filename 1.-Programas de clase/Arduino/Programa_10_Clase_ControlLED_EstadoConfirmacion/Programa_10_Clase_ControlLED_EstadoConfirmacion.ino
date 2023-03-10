int led=2;
int estado;

void setup() {
  pinMode(led,OUTPUT);
  Serial.begin(9600);
  Serial.setTimeout(100);//ms por defecto son 1000
}

void loop() {
  if(Serial.available()>0){
    estado = Serial.readString().toInt();
    Serial.println(String(estado));
    digitalWrite(led,estado);
  }
  delay(10);
}
