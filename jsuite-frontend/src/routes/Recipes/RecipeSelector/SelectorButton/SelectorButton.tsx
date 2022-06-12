import { Button } from "./SelectorButton.styles";

const SelectorButton = (props: any) => {
  return <div>
    <Button onClick={() => props.handleClick()} id={`selector-button-${props.id}`}>{props.title}</Button>
    </div>;
};

export default SelectorButton;
