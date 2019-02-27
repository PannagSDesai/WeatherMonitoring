void setup() {
  pinMode(10, OUTPUT);
  pinMode(2,INPUT);
  pinMode(4,INPUT);
  pinMode(7,INPUT);
  pinMode(8,INPUT);
  pinMode(3,OUTPUT);
  pinMode(5,OUTPUT);
  pinMode(6,OUTPUT);
  pinMode(13,OUTPUT);
}
void pwm(int PIN){
  int i=0;
  for(i=0;i<=50;i++){
  analogWrite(PIN,i);
  delay(30);
  }
}
void flashhard(int PIN){
  for(int j=0;j<=2;j++){
  digitalWrite(PIN,HIGH);
  delay(50);
  digitalWrite(PIN,LOW);
  delay(50);
  }
}
void psmsoft(int PIN){
  for(int i=2;i<=50;i++){
  analogWrite(PIN,i);
  delay(30);
}
}
char msg;
void loop() {
  char a,b,c,d;
  a=digitalRead(2);
  b=digitalRead(4);
  c=digitalRead(7);
  d=digitalRead(8);
  delay(2);
  if (a==0 && b==0 && c==0 && d==0)
  msg=1;
  else if (a==1 && b==0 && c==0 && d==0)
  msg=2;
  else if (a==1 && b==1 && c==0 && d==0)
  msg=3;
  else if (a==1 && b==1 && c==1 && d==0)
  msg=4;
  else if (a==0 && b==0 && c==0 && d==1)
  msg=5;
  else if (a==0 && b==0 && c==1 && d==1)
  msg=6;
  else if (a==0 && b==1 && c==1 && d==1)
  msg=7;
  else if (a==1 && b==1 && c==1 && d==1)
  msg=8;
  else if (a==0 && b==0 && c==1 && d==0)
  msg=9;
  else if(a==0 && b==1 && c==0 && d==0)
  msg=10;
  switch(msg){
  case 1:
  digitalWrite(10,HIGH);
  break;
  case 2:
  flashhard(5);
  break;
  case 3:
  psmsoft(6);
  pwm(3);
  break;
  case 4:
  flashhard(3);
  case 5:
  flashhard(3);
  pwm(13);
  break;
  case 6:
  psmsoft(13);
  flashhard(3);
  break;
  case 7:
  pwm(13);
  break;
  case 8:
  psmsoft(3);
  break;
  case 9:
  pwm(3);
  break;
  case 10:
  digitalWrite(13,HIGH);
  delay(1000);
  digitalWrite(13,LOW);
  delay(1000);
  break;
  }
  }
