PShape torso;
PShape shoulderFR, shoulderFL, shoulderBR, shoulderBL;
PShape femurFR, femurFL, femurBR, femurBL;
PShape footFR, footFL, footBR, footBL;
float rotX, rotY;
float alpha = -1, beta = -2, gamma;

//Leg 1 = FR
float theta1, theta2, theta3 = 0;

//Leg 2 = BR
float theta4, theta5, theta6 = 0;

//Leg 3 = FL
float theta7, theta8, theta9 = 0;

//Leg 4 = BL
float theta10, theta11, theta12 = 0;

void setup(){
  size (1200,800,OPENGL);
  
  torso = loadShape("nanotorso.obj");
  
  shoulderFR = loadShape("shoulder.obj");
  shoulderFL = loadShape("shoulder.obj");
  shoulderBR = loadShape("shoulder.obj");
  shoulderBL = loadShape("shoulder.obj");
  
  femurFR = loadShape("femurright.obj");
  femurBL = loadShape("femurright.obj");
  femurFL = loadShape("femurleft.obj");
  femurBR = loadShape("femurleft.obj");
  
  footFR = loadShape("footright.obj");
  footBL = loadShape("footright.obj");
  footFL = loadShape("footleft.obj");
  footBR = loadShape("footleft.obj");
  
  torso.disableStyle();
  femurFR.disableStyle();
  femurFL.disableStyle();
  femurBR.disableStyle();
  femurBL.disableStyle();
  //loArm.disableStyle();
  
  
}

void draw(){
  background(32);
  smooth();
  lights();
  directionalLight(51, 102, 126, -1, 0, 0);
  
  //fill (#FF9F03);
  //fill (#FFE308);
  //fill(#2F4F4F);
  //fill(#FF4500); orange
  //fill(#87CEFA); light blue
  fill(#76eec6);
  noStroke();
  
  
  translate (width/2,height/2);
  scale(-4);
  //rotateX(PI);
  //rotateY(PI);
  //translate(0,-40,0);
  
  rotateX(rotX);
  rotateY(-rotY);
  shape(torso);
  //box(300);
  //rect(100,100,500,500);
  
  //=======================TARGET PRACTICE====================
  translate(-100,-100,-100);
  sphere(10);
  translate(100,100,100);
  
  //=======================LEG FR====================
  
  //x=58.71 - good
  //z=-48.155+1.5
  //y=1.22383
  translate(57.255,0,-48.155);
  //rotateY(gamma);
  //Theta1 is the commanded angle
  rotateX(theta1);
  shape(shoulderFR);
  
  translate(0,0,-6.13);
  rotateZ(theta2);
  shape(femurFR);
  
  theta3+=0.005;
  translate(5.092,-44.1167,0);
  rotateX(theta3);
  shape(footFR);
  
  //Normalize shifts
  rotateX(-theta3);
  translate(-5.092,44.1167,0);
  rotateZ(-theta2);
  translate(0,0,6.13);
  rotateX(-theta1);
  translate(-57.255,0,48.155);
  
  //=========================END FR=======================
  
  //Return to center
  //translate(-5.092,44.1167,0);
  //translate(0,0,6.13);
  //translate(-57.255,0,48.155);
  
  //=====================LEG BL=========================
  
  //Move to BL position
  translate(-57.255,0,48.155);
  rotateX(PI);
  rotateZ(PI);
  
  rotateX(theta4);
  shape(shoulderBR);
  
  translate(0,0,-6.13);
  rotateZ(theta5);
  shape(femurBL);
  
  translate(5.092,-44.1167,0);
  theta6 += 0.005;
  rotateX(theta6);
  shape(footFR);
  //===================END BL===========================
  
  //Return to center
  rotateX(-theta6);
  translate(-5.092,44.1167,0);
  rotateZ(-theta5);
  translate(0,0,6.13);
  rotateX(-theta4);
  
  //rotateZ(-PI);
  rotateX(-PI);
  translate(57.255,0,-48.155);
  
  //=====================LEG FL=========================
  
  //Move to FL position
  translate(-57.255,0,-48.155);
  theta7 = -PI/24;
  rotateX(theta7);
  shape(shoulderFL);
  
  //translate(-2*58.71,0,0);
  //rotateZ(PI);
  //rotateX(beta);
  translate(0,0,-6.13);
  theta8 = -PI/6 + PI/24;
  rotateZ(theta8);
  shape(femurFL);
  
  translate(5.092,44.1167,0);
  theta9=-PI/6 + -PI/12;
  rotateX(theta9);
  shape(footFL);
  
  //=====================END FL=========================
  
  rotateX(-theta9);
  translate(-5.092,-44.1167,0);
  rotateZ(-theta8);
  translate(0,0,6.13);
  rotateX(-theta7);
  translate(-57.255,0,48.155);
  
  //=====================LEG BR=========================
  translate(-57.255,0,48.155);
  //rotateY(gamma);
  rotateZ(PI);
  rotateX(PI);
  
  rotateX(theta10);
  shape(shoulderBR);
  
  translate(0,0,-6.13);
  rotateZ(theta11);
  shape(femurBR);
  
  translate(5.092,44.1167,0);
  theta12+=0.005;
  rotateX(theta12);
  shape(footBR);
  
}

void mouseDragged(){
  rotY -= (mouseX - pmouseX) * 0.01;
  rotX -= (mouseY - pmouseY) * 0.01;
}