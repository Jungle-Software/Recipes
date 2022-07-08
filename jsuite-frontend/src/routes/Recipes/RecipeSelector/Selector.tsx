import { RecipeId } from "../../../models/Recipe";
import { SelectorList } from "./Selector.styles";
import SelectorButton from "./SelectorButton/SelectorButton";

type Props = {
  recipeIds: RecipeId[];
  onRecipeChange: Function;
}

const Selector = (props: Props) => {

  return (
    <SelectorList>
      {props.recipeIds.map((recipe: any) => (
        <SelectorButton
          id={recipe.id}
          key={recipe.id}  // This is not actually a prop, hence why I had to add id separately
          title={recipe.title}
          handleClick={() => props.onRecipeChange(recipe.id)}
        />
      ))}
    </SelectorList>
  );
};

export default Selector;
