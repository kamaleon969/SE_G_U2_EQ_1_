int potenciometro = A0;
int tamMuestra = 30;

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
}

int valMenor = 9999;
int i,valor;
void loop() {
  // put your main code here, to run repeatedly:
  //Preprocesamiento de datos...
  for(i=0;i<tamMuestra; i++){
    valor = analogRead(potenciometro); //buscar dismunuir el efecto del ruido
    Serial.println(valor);

    if(valor<valMenor){
      valMenor = valor;
    }
  }

  //Serial.println("Valor=" + String(valor));
  Serial.println(valMenor);
  delay(1000);
}
