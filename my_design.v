
module my_design( input a,b,c,e,f,g,s ,clk ,output reg q);
    wire w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,d ;
    
    
    and u1 (w1,a,b);
    and u2  (w2,a,c);
    and u3 (w3,b,c);
    or u4 (w7,w1,w2,w3);
    
    and v1 (w4,e,f);
    and v2  (w5,e,g);
    and v3 (w6,f,g);
    or v4 (w8,w4,w5,w6);
    
    not p1 (w9,s);
    and p2 (w10,w9,w7);
    and p3  (w11,w8,s);
    or p4 (d,w10,w11);
    
    always @(posedge clk)
    begin
        q<=d;
        
 end
 endmodule

