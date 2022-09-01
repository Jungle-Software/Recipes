import { gql, useMutation } from "@apollo/client";
import DevError from "../../../../../components/DevError/DevError";
import { Button } from "./SelectorDeleteButton.styles";

export const DELETE_RECIPE_BY_ID_QUERY = gql`
    mutation DeleteRecipe($id: ID!) {
            deleteRecipe (id: $id) {
                recipe {
                id
            }
        }
    }
`;

type Props = {
    id: number
    handleClick: Function
}

const SelectorDeleteButton = (props: Props) => {
    const [deleteRecipe, { data, loading, error }] = useMutation(DELETE_RECIPE_BY_ID_QUERY, {
        variables: { id: props.id },
        onCompleted() {
            props.handleClick(props.id)
        },
        onError() {}
      });

    if (loading) return <div>Deleting...</div>;
    if (error) return <DevError message={error.message}></DevError>; 
    if (data) return <div>Deleted!</div> // TODO maybe show a snackbar or something on fail/success (part of UI task)


    return (
        <Button 
            onClick={() => {deleteRecipe()}}
            id={`delete-button-${props.id}`}
        >DELETE</Button>
      )
}

export default SelectorDeleteButton;