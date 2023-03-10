int Pot=A0;

void setup() {
  Serial.begin(9600);
}

int valor;
void loop() {
  valor=analogRead(Pot);
  //Serial.println("Valor: "+String(valor)); //Pierde velocidad en arduino con caracteres
  Serial.println(valor);
  delay(1000);
}
