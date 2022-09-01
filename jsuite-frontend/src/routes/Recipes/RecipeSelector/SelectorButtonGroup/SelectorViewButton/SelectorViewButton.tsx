import { RecipeId } from "../../../../../models/Recipe";
import { Button } from "./SelectorViewButton.styles";

type Props = {
  recipe: RecipeId
  handleClick: Function
}
const SelectorViewButton = (props: Props) => {
  return (
    <Button onClick={() => props.handleClick()} id={`selector-button-${props.recipe.id}`}>{props.recipe.title}</Button>
  )
};

export default SelectorViewButton;
