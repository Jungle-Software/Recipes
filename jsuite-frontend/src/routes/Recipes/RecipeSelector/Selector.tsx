import { SelectorList } from "./Selector.styles";
import SelectorButton from "./SelectorButton/SelectorButton";

const Selector = (props: any) => {

  return (
    <SelectorList>
      {props.recipes.map((recipe: any) => (
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
