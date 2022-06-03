import { SelectorList } from "./Selector.styles";
import SelectorButton from "./SelectorButton/SelectorButton";

const Selector = (props: any) => {

  return (
    <SelectorList>
      {props.recipeIDs.map((recipe: any) => (
        <SelectorButton
          key={recipe.id}
          title={recipe.title}
          handleClick={() => props.onRecipeChange(recipe.id)}
        />
      ))}
    </SelectorList>
  );
};

export default Selector;
