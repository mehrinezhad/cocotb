
    
             
import cocotb
from cocotb.result import TestFailure
from cocotb.triggers import Timer
import random
@cocotb.test()

def test_my_design(dut):
    
    for dut.s in[0,1]:
        for dut.a in [0,1]:
            for dut.b in [0,1]:
                for dut.c in [0,1]:
                    for dut.e in [0,1]:
                        for dut.f in [0,1]:
                           for dut.g in [0,1]:
                               yield Timer(1,"ns")

                               
                                   
                                   
                                #-----------------------------------------------------------
                                #-----------------------------------------------------------

                               if dut.a == 1 and dut.b == 1 and dut.c==1:
                                    w7=1
                                            
                               #-------------------------------------------------------------  
                               elif dut.a==1 and dut.b==1 and  dut.c==0:
                                    w7=1
                                        
                                            
                                #-------------------------------------------------------------     
                               elif dut.a==1 and dut.b==0 and dut.c==1:
                                    w7=1
                                        
                                #-------------------------------------------------------------
                               elif dut.a==1 and dut.b==0 and dut.c==0:
                                    w7=0
                                        
                                #------------------------------------------------------------- 
                               elif dut.a== 0 and dut.b == 1 and dut.c==1:
                                    w7=1
                                        
                                            
                                #-------------------------------------------------------------
                               elif  dut.a == 0 and dut.b == 1 and dut.c==0:
                                    w7=0
                                  
                                #-------------------------------------------------------------
                               elif dut.a == 0 and dut.b == 0 and dut.c==1:
                                    w7=0
                                        
                                #-------------------------------------------------------------
                               elif dut.a == 0 and dut.b ==0 and dut.c==0:
                                    w7=0
                                        
                                                                       
            

                    
                                #-----------------------------------------------------------
                                #-----------------------------------------------------------

                               if dut.e == 1 and dut.f == 1 and dut.g==1:
                                    w8=1
                                            
                                #-------------------------------------------------------------  
                               elif dut.e==1 and dut.f==1 and  dut.g==0:
                                    w8=1
                                        
                                            
                                #-------------------------------------------------------------     
                               elif dut.e==1 and dut.f==0 and dut.g==1:
                                    w8=1
                                        
                                #-------------------------------------------------------------
                               elif dut.e==1 and dut.f==0 and dut.g==0:
                                    w8=0
                                        
                                #------------------------------------------------------------- 
                               elif dut.e== 0 and dut.f == 1 and dut.g==1:
                                    w8=1
                                        
                                            
                                #-------------------------------------------------------------
                               elif  dut.e == 0 and dut.f == 1 and dut.g==0:
                                    w8=0
                                  
                                #-------------------------------------------------------------
                               elif dut.e == 0 and dut.f == 0 and dut.g==1:
                                    w8=0
                                        
                                #-------------------------------------------------------------
                               elif dut.e == 0 and dut.f==0 and dut.g==0:
                                    w8=0
                                #------------------------------------------------------------
                                #------------------------------------------------------------

                               if dut.s==0 :
                                   d=w7

                               elif dut.s==1 :
                                   d=w8
                                #------------------------------------------------------------
                                #------------------------------------------------------------


                               yield Timer(1,"ns")
                               dut.clk.value=1
                               yield Timer(1,"ns")
                               dut.clk.value=0


                               if dut.q != d :
                                   raise TestFailure("Failure!")

                                










                                   

                               

                                   

                                

                                    
                                    

                           




                                   
                   
                               

                                
                               

                
