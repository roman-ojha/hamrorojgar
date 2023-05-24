export function isOkResponse(status: number): boolean {
  if (status >= 200 && status < 300) {
    return true;
  }
  return false;
}
