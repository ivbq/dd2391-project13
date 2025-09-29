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
        agent: navigator.userAgent,
        // geolocation: location,
        languages: navigator.languages
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