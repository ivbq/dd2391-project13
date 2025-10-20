# dd2391-project13

## Introduction - Browser Fingerprinting

There are many situation in which servers or applications needs, or wants to,
identify users. Subscription services rely on limiting subscription sharing to increase revenue, forums may want to use identification to enforce blacklists and law enforcement organisation may use identification as a mean to track individuals. It is clear that user tracking without consent of the individual can both be used in good ways and bad ways. What is a good use and what is a bad use is in the eye of the beholder.

Tracking of users has many established methods, such as logging in to access features and IP tracking. IP tracking is usually spoofed by VPN-services and forcing the user to log in does not prevent account sharing. Another way to track users is by *fingerprinting*, that is finding and formalizing attributes that differs between users. When looking for attributes, if one wants to avoid the possibillity of spoofing, it is possible to narrow down attributes that are hard to mimic or change.

Browser settings are commonly set in stone for a normal user. Local browser attributes are possible to spoof, but often comes with a downside of a worsened user experience. Hence, it is a set of attributes that is interesting to use for user identification.

### Problem statement

Given a set of users, where each user has a unique composition of browser attributes, is it possible to use Browser Fingerprinting to differentiate all the users?


## References

We've referred to MDN's (https://developer.mozilla.org) extensive JavaScript and general web technology documentation for implementing most of our fingerprinting methods. The testing suite is written using Playwright (https://playwright.dev/docs/), whose documentation we have also referred to during the development process.

## Background

There is no correct way to establish a fingerprint on a browser, but it is clear that the absolute goal of such a fingerprint is to identify and seperate each unique user. However there is a limitied set of attributes, espacially when said attributes come with default values, there is no guarantee to be able to identify any user. Simply by the pigeon hole principle, a fingerprint can only identify as many unique users as there is combinations of the attributes. For instance, if there are 15 independent boolean attributes, there is only $2^{15} = 32768$ possible *identities*.

However, increasing the number of attributes quickly increases the number of possible *identities*. For each boolean attribute added, it doubles the number of possible *identities*. There is also attributes which arent boolean, such as the screen. Although it is uncommon to use non-standard screen resolutions, in theory, using the screen size up to 1920x1080 as a fingerprint would increase the number of *identities* by a factor of $1920*1080 = 2073600$. That is a factor of 2 million.

Storing, or transmitting, browser fingerprints must also be taken into consideration. Storing the raw attributes leads to overhead and could therefore have a large impact on storage capabillities and application. One possible way to reduce the overhead for the application is to generate a hashed fingerprint on the client-side.


## Solution

## Testing

To test if our built solution is able to fulfill the problem, the testing script generates a set of users, each user with unique browser attributes. The program than fetches the browser fingerprint for each users and stores them. The last phase of testing consists of finding duplicates of any fingerprint. If the program can not find any duplicates, we conclude that the problem is solved for the user set. Otherwise, we conclude that the implemnted browser fingerprint application does not suffice to identify the generated user set.

It is important to notice, that the generated user set is not representive of the average set of users that connect to an application. Nor is the generated set exhaustive, meaning that there could be a composition of browser attributes that generates a fingerprint that has already been generated.


## Usage

### Fingerprint of a single browser
To obtain a browser fingerprint you open `index.html` in your browser. The tests should be supported on all modern platforms.

To run the test framework you first have to install Python3, then Playwright locally using the following commands:
`pip install playwright`
`py -m playwright install`

Then 