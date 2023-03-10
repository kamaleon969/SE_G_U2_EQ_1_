
int sensor1 = A0,sensor2 = A1,sensor3 = A2;

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(10);
}

int sA,sB,sC;
void loop() {
  sA=analogRead(sensor1);
  sB=analogRead(sensor2);
  sC=analogRead(sensor3);

  //Armar la cadena que se enviara
  String cadena = "P"+String(sA)+""+String(sB)+""+String(sC)+"K";
  Serial.println(cadena);
  delay(500);
}
