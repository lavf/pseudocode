
einkommen_miete = [
    [4200.0, 1200.0],
    [ 900.0,  340.0],
    [1800.0,  600.0],
    [3600.0, 1100.0],
    [2700.0,  800.0],
    [5900.0, 1300.0]
]


def prozente(einkommen_miete):
    prozente            = [0,0,0,0,0]
    mieteProGruppe      = [0,0,0,0,0]
    einkommenProGruppe  = [0,0,0,0,0]
    i = 0
    j = 0

    while i < len(einkommen_miete):
        if einkommen_miete[i][0] < 1000:
            einkommenProGruppe[0] = einkommenProGruppe[0] + einkommen_miete[i][0]
            mieteProGruppe[0]     = mieteProGruppe[0] + einkommen_miete[i][1]
        elif einkommen_miete[i][0] >= 1000 and einkommen_miete[i][0] <= 1999:
            einkommenProGruppe[1] = einkommenProGruppe[1] + einkommen_miete[i][0]
            mieteProGruppe[1]     = mieteProGruppe[1] + einkommen_miete[i][1]
        elif einkommen_miete[i][0] >= 2000 and einkommen_miete[i][0] <= 2999:
            einkommenProGruppe[2] = einkommenProGruppe[2] + einkommen_miete[i][0]
            mieteProGruppe[2]     = mieteProGruppe[2] + einkommen_miete[i][1]
        elif einkommen_miete[i][0] >= 3000 and einkommen_miete[i][0] <= 3999:
            einkommenProGruppe[3] = einkommenProGruppe[3] + einkommen_miete[i][0]
            mieteProGruppe[3]     = mieteProGruppe[3] + einkommen_miete[i][1]
        else:
            einkommenProGruppe[4] = einkommenProGruppe[4] + einkommen_miete[i][0]
            mieteProGruppe[4]     = mieteProGruppe[4] + einkommen_miete[i][1]
        i = i + 1
    
    while j < len(prozente):
        prozente[j] = mieteProGruppe[j] * 100 / einkommenProGruppe[j]
        j = j + 1
    
    return prozente

prozenteArray = prozente(einkommen_miete)

print(prozenteArray)
