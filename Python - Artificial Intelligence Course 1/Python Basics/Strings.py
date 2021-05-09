s = "String çalışma alanı"

varType = type(s) #type fonksiyonu değişkenin tipini döndürür.
print(varType)

print(s)

s1 = "Bar"
s2 = "celona"
s3 = s1+s2
print(s3) #Barcelona

lenght = len(s3) # len fonksiyonu string değişkenin uzunluğunu verir.

s1First = s3[0] # Stringlerde aslında birer listedir. Bu şekilde string değişkenlerin belirtilen elemanına ulaşırız.
print(s1First) # B