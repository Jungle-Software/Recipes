import { RecipeId } from "../../../models/Recipe";
import { SelectorList } from "./RecipeSelector.styles";
import SelectorButtonGroup from "./SelectorButtonGroup/SelectorButtonGroup";

type Props = {
  recipeIds: RecipeId[];
  onRecipeSelect: Function;
  onRecipeDelete: Function;
}

const RecipeSelector = (props: Props) => {

  return (
    <SelectorList>
      {props.recipeIds.map((recipe: RecipeId) => (
        <SelectorButtonGroup 
          key={recipe.id}  // Not actually a prop. Needed for React warning
          recipe={recipe}
          onRecipeSelect={(recipeId: number) => props.onRecipeSelect(recipeId)}
          onRecipeDelete={(recipeId: number) => props.onRecipeDelete(recipeId)}
          />
      ))}
    </SelectorList>
  );
};

export default RecipeSelector;
