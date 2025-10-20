async function generateFingerprint() {
    // Get location
    // var location;
    // function success(pos) {
    //     location = pos.coords;
    // }
    // function error() {
    //     location = "Location not shared."
    // }
    // navigator.geolocation.getCurrentPosition(success, error)

    // Generate fingerprint
    const fingerprint = {
        // Properties-based fingerprinting
        agent: navigator.userAgent,
        platform: navigator.platform,
        languages: navigator.languages,
        timezone: Intl.DateTimeFormat().resolvedOptions().timeZone,
        screen: {
            width: screen.width,
            height: screen.height,
            colorDepth: screen.colorDepth,
            pixelDepth: screen.pixelDepth,
            availWidth: screen.availWidth,
            availHeight: screen.availHeight
        },
        doNotTrack: navigator.doNotTrack,

        // Advanced fingerprinting
        permissions: await getPermissions(),
        cookies: await getCookieFingerprint(),
    }
    return fingerprint;
}

async function hashFingerprint(fingerprint) {
    const str = JSON.stringify(fingerprint);
    const buffer = new TextEncoder().encode(str);
    const hashBuffer = await crypto.subtle.digest('SHA-256', buffer);
    const hashArray = Array.from(new Uint8Array(hashBuffer));
    const hashHex = hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
    return hashHex;
}

async function getCookieFingerprint()
{
    //Kontroll om cookie är avstängd
    const enabled=navigator.cookieEnabled;//browser-inställning
    let test=false;
    try
    {
        document.cookie="Test_cookie=1",
        test=document.cookie.indexOf("Test_cookie") ! == -1;
        
    }

    //kontroll om vi kan läsa cookie:

}


async function getPermissions() {
    const permissions = [
        "accelerometer",
        "accessibility-events",
        "ambient-light-sensor",
        "background-sync",
        "camera",
        "clipboard-read",
        "clipboard-write",
        "geolocation",
        "gyroscope",
        "local-fonts",
        "magnetometer",
        "microphone",
        "midi",
        "notifications",
        "payment-handler",
        "persistent-storage",
        "push",
        "screen-wake-lock",
        "storage-access",
        "top-level-storage-access",
        "window-management",
    ];
    let permissionStatus = [];
    for (const permission of permissions) {
        try {
            let res;
            if (permission === "top-level-storage-access") {
                res = await navigator.permissions.query({
                    name: permission,
                    requestedOrigin: window.location.origin,
                });
            } else {
                res = await navigator.permissions.query({ name: permission });
            }
            permissionStatus.push(res.state);
        }
        catch (error) {
            permissionStatus.push('Not supported');
        }
    }
    return permissionStatus;
}
