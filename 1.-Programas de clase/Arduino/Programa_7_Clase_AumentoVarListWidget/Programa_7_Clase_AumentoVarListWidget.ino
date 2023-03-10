int Variable;

void setup() {
  Variable=0;
  Serial.begin(9600);
}

void loop() {
  Serial.println(Variable);
  Variable++;
  delay(500);
}
