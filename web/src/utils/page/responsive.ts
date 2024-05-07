export const getHeightWithoutHeader = () => {
  const header = document.querySelector("#header");
  return window.innerHeight - (header ? header.clientHeight : 0);
};
