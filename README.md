# dd2391-project13

## Background - Browser Fingerprinting

There are many situation in which servers or applications needs, or wants to,
identify users. Subscription services relay on limiting account sharing to increase revenue
### Problem statement

Is it possible to design a client-side Browser Fingerprinting application to identify users with unique composition of browser attributes?

## References

We've referred to MDN's (https://developer.mozilla.org) extensive JavaScript and general web technology documentation for implementing most of our fingerprinting methods. The testing suite is written using Playwright (https://playwright.dev/docs/), whose documentation we have also referred to during the development process.

## Testing

There is no correct way to establish a fingerprint on users, but it is clear that the absolute goal of such a fingerprint is to identify and seperate each unique user. However given limitied attributes, espacially when said attributes come with default values, there is no guarantee to be able to identify any user. Simply by the pigeon hole principle, a fingerprint can only identify as many unique users as there is combinations of the attributes. For instance, if there are 15 independent boolean attributes, there is only $2^{15} = 32768$ possible *identities*.

It's infeasible to test if there are enough unique *identies* to cover a targeted userbase. It is however, possible to test each attribute by it self. If each attribute can  

## Usage

To obtain a browser fingerprint you open `index.html` in your browser. The tests should be supported on all modern platforms.

To run the test framework you first have to install Python3, then Playwright locally using the following commands:
`pip install playwright`
`py -m playwright install`