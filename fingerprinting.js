async function generateFingerprint() {
    const fingerprint = {
        agent: navigator.userAgent
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