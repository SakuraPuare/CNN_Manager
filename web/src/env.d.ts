declare module "*.vue" {
  import { DefineComponent } from "vue";
  const component: DefineComponent<
    NonNullable<unknown>,
    NonNullable<unknown>,
    unknown
  >;
  export default component;
}
