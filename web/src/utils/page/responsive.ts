export const getHeightWithoutHeader = () => {
  const header = document.querySelector("#header");
  const height = window.innerHeight - (header ? header.clientHeight : 0);
  return height;
};
