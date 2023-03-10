int Pot=A0;

void setup() {
  Serial.begin(9600);
}

int valor,i;
void loop() {

  for(i=0;i<10;i++){
    valor+=analogRead(Pot);
  }
  valor/=10;
  Serial.println(valor);
  delay(1000);
}
