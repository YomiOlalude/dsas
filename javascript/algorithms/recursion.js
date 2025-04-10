const flattenArray = (array) => {
  if (array.length <= 0) {
    return []
  }

  if (array[0] instanceof Array) {
    return flattenArray(array[0]).concat(flattenArray(array.slice(1,)))
  }

  return [array[0]].concat(flattenArray(array.slice(1,)))
}