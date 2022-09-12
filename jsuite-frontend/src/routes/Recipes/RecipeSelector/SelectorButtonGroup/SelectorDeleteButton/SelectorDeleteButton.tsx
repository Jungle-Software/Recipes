import { gql, useMutation } from "@apollo/client";
import DevError from "../../../../../components/DevError/DevError";
import { RecipeId } from "../../../../../models/Recipe";
import { Button } from "./SelectorDeleteButton.styles";

export const DELETE_RECIPE_BY_ID_MUTATION = gql`
    mutation DeleteRecipe($id: ID!) {
            deleteRecipe (id: $id) {
                recipe {
                id
            }
        }
    }
`;

const handleDelete = (recipe: RecipeId, deleteRecipe: Function) => {
    if (window.confirm(`Are you sure you want to delete '${recipe.title}'?`)) {
        deleteRecipe()
    }
}

type Props = {
    recipe: RecipeId
    handleClick: Function
}

const SelectorDeleteButton = (props: Props) => {
    const [deleteRecipe, { data, loading, error }] = useMutation(DELETE_RECIPE_BY_ID_MUTATION, {
        variables: { id: props.recipe.id },
        onCompleted() {
            props.handleClick(props.recipe.id)
        },
        onError() {}
      });

    if (loading) return <div>Deleting...</div>;
    if (error) return <DevError message={error.message}></DevError>; 
    if (data) return <div>Deleted!</div> // TODO maybe show a snackbar or something on fail/success (part of UI task)


    return (
        <Button 
            onClick={() => handleDelete(props.recipe, deleteRecipe)}
            id={`delete-button-${props.recipe.id}`}
        >DELETE</Button>
      )
}

export default SelectorDeleteButton;