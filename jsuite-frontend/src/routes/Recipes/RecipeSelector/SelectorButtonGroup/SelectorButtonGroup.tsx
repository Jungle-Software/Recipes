import SelectorViewButton from "./SelectorViewButton/SelectorViewButton";
import SelectorDeleteButton from "./SelectorDeleteButton/SelectorDeleteButton";
import { RecipeId } from "../../../../models/Recipe";

type Props = {
    recipe: RecipeId
    onRecipeSelect: Function,
    onRecipeDelete: Function
}

const SelectorButtonGroup = (props: Props) => {

    return (<div>
        <SelectorViewButton
            recipe={props.recipe}
            handleClick={() => props.onRecipeSelect(props.recipe.id)}
        />
        <SelectorDeleteButton
            id={props.recipe.id}
            handleClick={(recipeId: number) => props.onRecipeDelete(recipeId)}
        />
    </div>
    );
};

export default SelectorButtonGroup;
