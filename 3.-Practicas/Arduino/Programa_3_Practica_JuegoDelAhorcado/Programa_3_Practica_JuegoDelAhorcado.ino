int Pulsador1 = 4 , Pulsador2 = 3, Pulsador3 = 2;

void setup() {
  pinMode(Pulsador1,INPUT_PULLUP);
  pinMode(Pulsador2,INPUT_PULLUP);
  pinMode(Pulsador3,INPUT_PULLUP);
  Serial.begin(9600);
  Serial.setTimeout(10);
}

int sA,sB,sC;
void loop() {
  sA=digitalRead(Pulsador1)==1?0:1;
  sB=digitalRead(Pulsador2)==1?0:1;
  sC=digitalRead(Pulsador3)==1?0:1;

  //Armar la cadena que se enviara
  String cadena = String(sA)+" "+String(sB)+" "+String(sC);
  Serial.println(cadena);
  delay(1000);
}
