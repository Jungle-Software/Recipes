import { SelectorList } from "./Selector.styles";
import SelectorButton from "./SelectorButton/SelectorButton";

const Selector = (props: any) => {

  return (
    <SelectorList>
      {props.recipeIDs.map((recipe: any) => (
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
