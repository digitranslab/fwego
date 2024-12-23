export default function addPublicAuthTokenHeader(config, publicAuthToken) {
  if (!config.headers) {
    config.headers = {}
  }
  config.headers['Fwego-View-Authorization'] = `JWT ${publicAuthToken}`
  return config
}
