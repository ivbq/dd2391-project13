# dd2391-project13

## Fingerprinting

Vi ska utveckla en webbsida som har olika typer av fingerprinting och se om vi kan motverka det med olika metoder.

Exempel:
Cookies - sumeya
Local storage
Browser identifier (vilken browser, version, etc) - Ivar
Locale, språk - only
Canvas - Jonathan

## Testing
There is no correct way to establish a fingerprint on users, but it is clear that the absolute goal of such a fingerprint is to identify and seperate each unique user. However given limitied attributes, espacially when said attributes come with default values, there is no guarantee to be able to identify any user. Simply by the pigeon hole principle, a fingerprint can only identify as many unique users as there is combinations of the attributes. For instance, if there are 15 independent boolean attributes, there is only $2^{15} = 32768$ possible *identities*.

It's infeasible to test if there are enough unique *identies* to cover a targeted userbase. It is however, possible to test each attribute by it self. If each attribute can  
`pip install playwright`
`py -m playwright install`