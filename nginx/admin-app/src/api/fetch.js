const DEF_URL = 'http://161.35.206.91:8080'
export const Fetch = (path, options) => {
  if (options.method !== 'GET' && options.method !== 'DELETE') {
    options.body = JSON.stringify(options.body)
  }
  const promise = new Promise((resolve, reject) => {
    fetch(`${DEF_URL}${path}`, {
      headers: {
        'Content-Type': 'application/json',
        Authorization:"Token " + localStorage.getItem("amazon_auth_token")
      },
      ...options
    })
      .then(response => {
        if (response.ok) {
          resolve(response.json())
        } else {
          reject(response)
        }
      })
      .catch(err => reject(err))
  })
  return promise
}

export const FetchAuth = (path, options) => {
  if (options.method !== 'GET' && options.method !== 'DELETE') {
    options.body = JSON.stringify(options.body)
  }
  const promise = new Promise((resolve, reject) => {
    fetch(`${DEF_URL}${path}`, {
      headers: {
        'Content-Type': 'application/json',
      },
      ...options
    })
      .then(response => {
        if (response.ok) {
          resolve(response.json())
        } else {
          reject(response)
        }
      })
      .catch(err => reject(err))
  })
  return promise
}
