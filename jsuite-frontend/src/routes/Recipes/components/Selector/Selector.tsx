import { SelectorList } from "./Selector.styles";
import { useEffect, useState } from "react";
import SelectorEl from "./components/SelectorEl/SelectorEl";

const Selector = (props: any) => {
  const firstRecipe = props.recipes ? props.recipes[0] : null;

  const [currentRecipe, setCurrentRecipe] = useState(firstRecipe);

  useEffect(() => {
    props.onRecipeChange(currentRecipe);
  }, [currentRecipe]);

  return (
    <SelectorList>
      {props.recipes.map((recipe: any) => (
        <SelectorEl
          key={recipe.id}
          title={recipe.title}
          handleClick={() => setCurrentRecipe(recipe)}
        />
      ))}
    </SelectorList>
  );
};

export default Selector;
