Shader "VertexLit Coloured" {
   Properties { _Color ("Main Colour", Color) = (1,1,1,1) } 
   
   SubShader { 
   CGPROGRAM
     #pragma surface surf Lambert

     struct Input { float4 color : COLOR; }; 
     uniform fixed4 _Color;

     void surf(Input IN, inout SurfaceOutput o) { 
       o.Albedo = IN.color.rgb;
       o.Alpha = 1;
     } 
   ENDCG
   }
 }