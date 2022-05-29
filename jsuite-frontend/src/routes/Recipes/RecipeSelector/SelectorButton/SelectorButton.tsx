import { Button } from "./SelectorButton.styles";

const SelectorButton = (props: any) => {
  return <div>
    <Button onClick={() => props.handleClick()}>{props.title}</Button>
    </div>;
};

export default SelectorButton;
