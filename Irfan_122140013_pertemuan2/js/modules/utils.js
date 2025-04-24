// Arrow function untuk simpan data
export const saveToStorage = (key, data) => localStorage.setItem(key, JSON.stringify(data));

// Arrow function untuk ambil data
export const getFromStorage = key => JSON.parse(localStorage.getItem(key)) || [];
