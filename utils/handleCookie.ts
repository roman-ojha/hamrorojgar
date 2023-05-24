function setCookie(name: string, value: string, days: number) {
  const expirationDate = new Date();
  expirationDate.setTime(expirationDate.getTime() + days * 24 * 60 * 60 * 1000);

  let cookieString = `${encodeURIComponent(name)}=${encodeURIComponent(value)}`;
  cookieString += `; expires=${expirationDate.toUTCString()}`;
  cookieString += `; path=/`;

  // Set Secure flag if using HTTPS
  if (window.location.protocol === "https:") {
    cookieString += "; Secure";
  }

  // Set HttpOnly flag
  cookieString += "; HttpOnly";
  cookieString += "; SameSite=None";

  document.cookie = cookieString;
}

function getCookie(name: string) {
  const cookieString = document.cookie;
  const cookies = cookieString.split(";");

  for (let i = 0; i < cookies.length; i++) {
    const cookie = cookies[i].trim();
    if (cookie.startsWith(`${name}=`)) {
      return decodeURIComponent(cookie.substring(name.length + 1));
    }
  }

  return null;
}

export { setCookie, getCookie };
