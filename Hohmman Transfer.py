import math

EarthRadius           = ((2*6378.1370)+6356.7523)/3
GravitationalConstant = 6.67430*10**-11
EarthMass             = (5.9722+0.0006)*10**24
objectMass            = 500 #kg

userInput_OrbitHeight_1 = float(input("Enter Orbital Height 1 in km: "))
userInput_OrbitHeight_2 = float(input("Enter Orbital Height 2 in km: "))

#Trasfer Ellipse Orbit
conversionValue1  = (((userInput_OrbitHeight_1+EarthRadius))*1000)                          #First Orbit
conversionValue2  = (((userInput_OrbitHeight_2+EarthRadius))*1000)                          #Second Orbit (transfer to)
semiMajorAxis     = (conversionValue1 + conversionValue2) / 2                               #Semi-Major Axis
eccentricity      = (conversionValue2-conversionValue1)/(conversionValue2+conversionValue1) #Eccentricity 
#print(semiMajorAxis)

class Calculation:
    calculatedValueV1 = math.sqrt((GravitationalConstant*EarthMass)/(conversionValue1))
    calculatedValueV2 = math.sqrt((GravitationalConstant*EarthMass)/(conversionValue2))
    cvV1_km           = calculatedValueV1/1000
    cvV2_km           = calculatedValueV2/1000
    #ME_OH1            = -(((GravitationalConstant*EarthMass*objectMass))/(2*(conversionValue1)))
    periapsisVelocity = math.sqrt(((GravitationalConstant*EarthMass)/conversionValue1)*(1+eccentricity*math.cos(0)))
    apoapasisVelocity = math.sqrt(((GravitationalConstant*EarthMass)/conversionValue2)*(1+eccentricity*math.cos(0)))
    deltaV1           = abs(periapsisVelocity - calculatedValueV1)
    deltaV2           = abs(calculatedValueV2 - apoapasisVelocity)
    deltaV_Total      = deltaV1 + deltaV2
    transferTime      = (math.sqrt(((4*(math.pi**2))/(GravitationalConstant*EarthMass))*(((conversionValue1+conversionValue2)/2)**3)))/2

arrayData = [
    Calculation.calculatedValueV1, 
    Calculation.calculatedValueV2, 
    Calculation.periapsisVelocity, 
    Calculation.apoapasisVelocity, 
    Calculation.deltaV1, 
    Calculation.deltaV2, 
    Calculation.deltaV_Total
    ]

labels = ['iOrbit-Vreq', 'fOrbit-Vreq', 'Periapsis Velocity', 'Apoapsis Velocity', 'DeltaV1', 'DeltaV2', 'Total DeltaV']

for label, value in zip(labels, arrayData):
    print(f"{label}: {value:,} m/s")

transferTime_Seconds = Calculation.transferTime
transferTime_Minutes = Calculation.transferTime/60
transfterTime_Hour   = Calculation.transferTime/3600
transferTime_Days    = transfterTime_Hour/24
print(f"Transfer Time: {transferTime_Seconds} Second(s) | {transferTime_Minutes} Minute(s) | {transfterTime_Hour} Hour(s) | {transferTime_Days} Day(s)")
#print(f"Mechanical Energy: {Calculation.ME_OH1:,} Kg*m^2/s^2")
