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
        permissions: await getPermissions(),
        languages: navigator.languages,
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
//function TestCookies()
{
    //SameSite
    document.cookie = "username=sumeya; path=/; SameSite=Strict; max-age=3600";
    document.cookie = "sessionID=789129aa; path=/; SameSite=Strict; max-age=3600";
    alert("Cookies have been set for testing.");
    location.reload();
}
//Cookies funktion
async function getCookieFingerprint()
{
    const cookies=document.cookie;
    return{
        hascookies: cookies.length>0,
        cookie: cookies ? cookies.split('; ').filter(c => c.trim()).length :0,
        cookieenable: navigator.cookieEnabled
    };
}
//Åtgärd 1. för att rensa cookies
async function clearCookies()
{
    const cookies = document.cookie.split("; ");
    for(let cookie of cookies)
        {
            const name=cookie.split("=")[0].trim();
            document.cookie = name + "=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/";
        }
        alert("Cookies have been cleared.");
        location.reload();
}
//Åtgärd 2. för att rensa cookie
//Kommer att köras i bakgrunden per automatik.
async function deleteCookie()
{
    setInterval(() => {
        clearCookies();
    }, 5000); // Rensa cookies var 5:e sekund
}

//Åtgärd 3. för att rensa cookie
async function SessionsOnlyCookies()
{
    const cookies = document.cookie.split("; ");

    cookies.forEach(cookie => {
        const [name,value]=cookie.split("=").map(s=> s.trim());
         document.cookie = `${name}=;expires=Thu, 01 Jan 1970 00:00:00 GMT;path=/`;
        // Skapa ny utan expires (= session-only)
        document.cookie = `${name}=${value};path=/;SameSite=Strict`;
    });
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
