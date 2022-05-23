import { SelectorBox } from "./SelectorEl.styles";

const SelectorEl = (props: any) => {
  return (
    <SelectorBox>
      <button onClick={() => props.handleClick()}>{props.title}</button>
    </SelectorBox>
  );
};

export default SelectorEl;
